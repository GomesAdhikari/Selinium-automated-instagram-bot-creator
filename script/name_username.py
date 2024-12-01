import random

def generate_random_name():
    first_names = [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Rohan", "Krishna", "Ishaan", "Shaurya",
        "Ananya", "Aarohi", "Diya", "Ira", "Myra", "Aditi", "Anika", "Saanvi", "Meera", "Sara",
        "Kabir", "Aryan", "Dev", "Om", "Kunal", "Harsh", "Yash", "Nikhil", "Tushar", "Rishi",
        "Shruti", "Pooja", "Neha", "Priya", "Aisha", "Riya", "Kavya", "Navya", "Swati", "Tara",
        "Raj", "Vikram", "Arvind", "Manoj", "Suresh", "Vivek", "Anil", "Sunil", "Rahul", "Amit",
        "Kiran", "Nidhi", "Preeti", "Bhavna", "Anita", "Deepa", "Seema", "Divya", "Amrita", "Lata",
        "Gaurav", "Siddharth", "Akash", "Ravi", "Sachin", "Naveen", "Ajay", "Varun", "Rakesh", "Armaan",
        "Simran", "Pallavi", "Juhi", "Madhavi", "Sheetal", "Poonam", "Vandana", "Alka", "Rashmi", "Mansi",
        "Mohit", "Abhishek", "Kartik", "Rajat", "Prateek", "Vishal", "Tarun", "Harish", "Lokesh", "Nirav",
        "Sonal", "Tanvi", "Rupali", "Bharti", "Manasi", "Sneha", "Monika", "Jaya", "Rekha", "Anuja"
    ]
    last_names = [
        "Sharma", "Verma", "Gupta", "Mehta", "Joshi", "Patel", "Reddy", "Iyer", "Chopra", "Kapoor",
        "Singh", "Khan", "Das", "Nair", "Rao", "Naik", "Ghosh", "Bose", "Chowdhury", "Mukherjee",
        "Mishra", "Pandey", "Srivastava", "Tripathi", "Dubey", "Thakur", "Yadav", "Agarwal", "Jain", "Saxena",
        "Tiwari", "Chatterjee", "Roy", "Sen", "Bhattacharya", "Banerjee", "Mahajan", "Kulkarni", "Deshmukh", "Gokhale",
        "Pawar", "Chavan", "Malhotra", "Bhat", "Shetty", "Menon", "Krishnan", "Ranganathan", "Prasad", "Venkatesh",
        "Sinha", "Lal", "Bhardwaj", "Dutta", "Chaturvedi", "Kashyap", "Rastogi", "Mathur", "Rawat", "Jadhav",
        "Kohli", "Grover", "Gill", "Dhillon", "Sodhi", "Ahluwalia", "Bedi", "Narang", "Puri", "Bagchi",
        "Rajput", "Kumar", "Rana", "Guha", "Pal", "Aggarwal", "Bajpai", "Kapadia", "Makhija", "Desai",
        "Gandhi", "Modi", "Parikh", "Shukla", "Kaul", "Bansal", "Dixit", "Chand", "Bora", "Sengupta",
        "Phadke", "Hegde", "Pillai", "Subramanian", "Raghavan", "Vasudevan", "Acharya", "Saha", "Ray", "De"
    ]

    first = random.choice(first_names)
    last = random.choice(last_names)
    fullname = first + ' ' + last
    while first == last:
        first = random.choice(first_names)
        last = random.choice(last_names)
    return first, last, fullname

# Function to generate a random username
def generate_username(first, last):
    random_number = random.randint(4965, 10009)
    return f"{first}{last}_{random_number}"
