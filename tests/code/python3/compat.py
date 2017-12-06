list_of_data = (
    bytes(data) if isinstance(data, memoryview) else data
    for data in list_of_data
)
