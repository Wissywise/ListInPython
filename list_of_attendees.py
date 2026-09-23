
"""Create a Python program that manages a list of attendees using lists, loops, if/else, and one small function.
Questions for this assignment
Create an initial list of 5 attendees and print the total count.
Add two late attendees and remove one person who withdrew, then print the updated list.
Print a numbered roster using a loop. If the name is your chosen lead (e.g., "Lucía"), tag it as “Lead” in the line.
Show slicing: print the first three names and the last two names.
Sort the list A–Z, print it, then reverse the order and print again.
Write a function find_attendee(name, roster) that returns "Found" or "Not Found" using a loop and if/else (no nesting).
Show two calls: one found, one not found.
Gemini said
This is a great exercise for mastering Python’s list manipulation and control flow. As a developer, you'll find that
managing collections of data like this is the bread and butter of most applications.
Here is the complete program broken down by your requirements.

1. Initializing and Modifying the List
We start by creating the list and using built-in methods like .append() and .remove() to update our attendees."""

# Create initial list of 5 attendees
attendees = ["Lucía", "Marcus", "Chen", "Sarah", "Diego"]
print(f"Initial count: {len(attendees)}")

# Add two late attendees
attendees.append("Amara")
attendees.append("Hiroshi")

# Remove one person who withdrew
attendees.remove("Diego")

print(f"Updated list: {attendees}")

# 2. Printing the Roster and Slicing To create a numbered list, we use enumerate. For slicing, we use the [start:stop] syntax.

# Print a numbered roster
print("\n--- Event Roster ---")
for index, name in enumerate(attendees, 1):
    # Check for the Lead (Lucía)
    if name == "Lucía":
        role = " - [Lead]"
    else:
        role = ""
    print(f"{index}. {name}{role}")

# Showing Slicing
print(f"\nFirst three names: {attendees[:3]}")
print(f"Last two names: {attendees[-2:]}")

# 3. Sorting and Reversing
"""
Python offers two ways to sort:.sort()(which changes the list permanently) and sorted()(which returns a new list).
We will use the permanent method here.
"""
# Sort A-Z
attendees.sort()
print(f"\nAlphabetical: {attendees}")

# Reverse the order (Z-A)
attendees.reverse()
print(f"Reverse Alphabetical: {attendees}")


# 4. The Search FunctionThis function avoids nested logic by using a straightforward loop and a conditional check.

def find_attendee(name, roster):
    """Checks if a specific name exists in the roster."""
    for person in roster:
        if person == name:
            return "Found"

    # This line only runs if the loop finishes without finding a match
    return "Not Found"


# Show two calls
print(f"\nSearching for 'Chen': {find_attendee('Chen', attendees)}")
print(f"Searching for 'Diego': {find_attendee('Diego', attendees)}")

"""
Summary of List Methods Used
Method       Action
len()        Returns the number of items in the list.
.append()    Adds an item to the very end.
.remove()    Finds and deletes a specific value.
[ :3]        Slices the list from index 0 up to (but not including) 3.
.sort()      Reorders the list alphabetically/numerically.
.reverse()   Flips the current order of the list.
"""