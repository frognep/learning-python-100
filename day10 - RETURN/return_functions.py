# functions with outputs

def format_name(last_name, first_name):
    if last_name == "" or first_name == "":
        return "No name inputted."
    formatted_last_name = last_name.title()
    formatted_first_name = first_name.title()
    formatted_name = f"{formatted_first_name} {formatted_last_name}"

    return formatted_name

print(format_name("NEP", "FROG"))
