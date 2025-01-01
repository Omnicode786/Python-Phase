# Consider the following scenario about using Python lists: 

# A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in the order they arrived in the classroom. Aniyah was the first one to note which students arrived, and then Imani took over. After class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one and sort it in alphabetical order. 

# Complete the code by combining the two lists into one and then sorting the new list. This function should:

# accept two lists through the function’s parameters;,

# combine the two lists;

# sort the combined list in alphabetical order;

# return the new list. 


def alphabetize_lists(list1, list2):


  new_list = [] # Initialize a new list.
  list2.extend(list1) # Combine the lists.
  list2.sort() # Sort the combined lists.
  new_list = list2 # Assign the combined lists to the "new_list".
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
