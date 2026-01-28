
import bpy
from typing import List, Callable, Optional, Any

def enum_callback(data: Any, old_var_name: str, new_var_name: str) -> Any:
    value = data[old_var_name] # Get value as int

    enum_definition = data.bl_rna.properties.get(new_var_name)

    if enum_definition and enum_definition.type == "ENUM":
        # Get the list of enum values and match by integer value
        for enum_item in enum_definition.enum_items:
            if value == enum_item.value:
                return enum_item.identifier
        
        # If no match found by value, try the first enum item as fallback
        if enum_definition.enum_items:
            print(f"Warning: Could not find enum value {value} for {new_var_name}, using first enum item")
            return enum_definition.enum_items[0].identifier
    
    print(f"Warning: Could not find enum definition for {new_var_name}")
    # Return the first enum item's identifier as a safe default
    if enum_definition and enum_definition.enum_items:
        return enum_definition.enum_items[0].identifier
    
    return value

def object_pointer_callback(data: Any, old_var_name: str, new_var_name: str) -> Any:
    value = data[old_var_name]
    if isinstance(value, bpy.types.Object):
        return value
    return None

class DataVariableUpdater:
    """
    A class to update data variables in Blender by renaming them.
    """
    def __init__(self):
        self.update_variable: int = 0
        self.remove_variable: int = 0
        self.print_log: bool = False

    def update_data_variable(self, data: Any, old_var_names: List[str], new_var_name: str, callback: Optional[Callable[[Any, str, str], Any]] = None):
        for old_var_name in old_var_names:
            if old_var_name in data:
                try:
                    if callback:
                        new_value = callback(data, old_var_name, new_var_name)
                        setattr(data, new_var_name, new_value)
                    else:
                        setattr(data, new_var_name, data[old_var_name])

                    del data[old_var_name]
                    print(f'"{old_var_name}" updated to "{new_var_name}" in {data.name}')
                except Exception as e:
                    print(f'Error updating "{old_var_name}" to "{new_var_name}" in {data.name}: {str(e)}')

    def remove_data_variable(self, data: Any, old_var_names: List[str]):
        for old_var_name in old_var_names:
            if old_var_name in data:
                try:
                    del data[old_var_name]
                    print(f'"{old_var_name}" removed from {data.name}')
                except Exception as e:
                    print(f'Error removing "{old_var_name}" from {data.name}: {str(e)}')

    def print_update_log(self):
        """
        Print a log of the number of data variables updated and removed.

        Args:
            None

        Returns:
            None
        """
        print(f'{self.update_variable} data variables have been updated.')
        print(f'{self.remove_variable} data variables have been removed.')