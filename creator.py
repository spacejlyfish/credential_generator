import random
#random occurence 1 = 100% 4 = 25% 10 = 10%
rand_prefix = 1
rand_suffix = 2
rand_between = 1
def load_names_from_file(filename):
    with open(filename, 'r') as f:
        return [name.strip() for name in f.readlines()]
def generate_password(name):
    current_year = str(datetime.datetime.now().year)[2:]  # Get the last two digits of the current year
    password = "!" + name[:4] + name[-4:] + current_year
    return password
def get_random_names(num_names):
    firstnames = load_names_from_file("firstname.txt")
    lastnames = load_names_from_file("lastname.txt")
    prefixes = load_names_from_file("prefix.txt")
    suffixes = load_names_from_file("suffix.txt")
    betweens = load_names_from_file("between.txt")

    generated_names = []
    used_firstnames = []
    used_lastnames = []
    passwords = []

    while len(generated_names) < num_names:
        first = random.choice(firstnames)
        last = random.choice(lastnames)
        name_parts = [first, last]

        # Track used first and last names
        used_firstnames.append(first)
        used_lastnames.append(last)

        # Add prefix
        if random.randint(1, rand_prefix) == 1: 
            prefix = random.choice(prefixes)
            name_parts.insert(0, prefix)

        # Add suffix
        if random.randint(1, rand_suffix) == 1:
            suffix = random.choice(suffixes)
            name_parts.append(suffix)

        # Add between
        if random.randint(1, rand_between) == 1:
            between = random.choice(betweens)
            name_parts.insert(1, between)

        full_name = "".join(name_parts) 
        generated_names.append(full_name)

        # Generate password for the name
        passwords.append(generate_password(full_name))

    return generated_names, used_firstnames, used_lastnames, passwords

if __name__ == "__main__":
    import datetime
    num_names = int(input("How many names do you want generated? "))
    #generated_names, used_firstnames, used_lastnames = get_random_names(num_names)
    generated_names, used_firstnames, used_lastnames, passwords = get_random_names(num_names)


    with open('outputusernames.txt', 'w') as f:
        for name in generated_names:
            f.write(name + '\n')

    with open('outputfirstnames.txt', 'w') as f:
        for first in used_firstnames:
            f.write(first + '\n')

    with open('outputlastnames.txt', 'w') as f:
        for last in used_lastnames:
            f.write(last + '\n')
    with open('outputpassword.txt', 'w') as f:
            for password in passwords:
                f.write(password + '\n')
    # Writing to outputmaster.txt
    with open('outputmaster.txt', 'w') as f:
        for i in range(len(generated_names)):
            master_line = f"{used_firstnames[i]}:{used_lastnames[i]}:{generated_names[i]}:{passwords[i]}\n"
            f.write(master_line)

    print(f"Generated names saved to outputusernames.txt, corresponding first names saved to outputfirstname.txt, corresponding last names saved to outputlastname.txt, and passwords saved to outputpassword.txt.")
