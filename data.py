def main():
    data = {'name': "ddd"}
    data_list = [data.copy() for _ in range(3)]  # Create copies to avoid unintended modification

    # Search for name "ggg"
    found_index = None
    for i, item in enumerate(data_list):
        if item['name'] == "ddd":
            found_index = i
            break

    # Update if found
    if found_index is not None:
        new_data = {'name': "updated_name"}  # Prepare the updated data
        data_list[found_index] = new_data  # Update the specific item
        print(f"Data updated at index {found_index}:", data_list)
    else:
        print("Name 'ggg' not found in the list.")


if __name__ == "__main__":
    main()
