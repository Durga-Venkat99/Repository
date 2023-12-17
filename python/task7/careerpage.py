class careerpage:
    def __init__(self):
        self.job_posts = []
        self.applications = []
    def add_job_post(self,title,description):
        job_post = joblisting(title,"",description)
        self.job_posts.append(job_post)
        return job_post
    
    def get_job_post(self):
        return self.job_post
    def get_application(self):
        return self.job_applications
    
class joblisting():
    def __init__(self,title,location,description):
        self.title = title
        self.location = location
        self.description = description

    def display_details(self):
        pass

class FullTimeJob(joblisting):
    def __init__(self, title, location, description, salary):
        super().__init__(title,location,description)
        self.salary = salary

    def display_details(self):
        return (f"FULL-Time job: {self.title} in {self.location}\n description: {self.description}\n Salary: {self.salary}")
    
class PartTimeJob(joblisting):
    def __init__(self,title, location, description,work_per_week):
        super().__init__(title,location,description)
        self.work_per_week = work_per_week

    def display_details(self):
        return (f"Part-Time job: {self.title} in {self.location}\n description: {self.description}\n work_per_week: {self.work_per_week}")

class Admin:
    def __init__(self,career_page):
        self.career = career_page
    def see_job_applicants(self):
        return self.career_page.get_applications   

class user:
    def __init__(self, career_page,name,email):
        self.career_page = career_page
        self.name = name
        self.email = email
    def apply_for_job(self,job_post):
        application = (self,job_post)
        self.career_page.applications.append(application)
    
    
    def view_job_listings(self):
        job_posts = self.career_page.get_job_posts()
        if job_posts:
            for i, job_post in enumerate(job_posts, start=1):
                print(f"{i}. {job_post.title}")
            choice = input("Enter the number of the job you want to view (or 'q' to quit): ")
            if choice == 'q':
                return
            try:
                choice = int(choice)
                if 1 <= choice <= len(job_posts):
                    print(job_posts[choice - 1].display_details())
                else:
                    print("Invalid choice. Please select a valid job listing.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
        else:
            print("No job listings available.")

# Concrete subclass of Person for an applicant
class Applicant(user):
    def introduce(self):
        return f"Applicant: {self.name}"

    @classmethod
    def interact(cls, user, job_listing):
        return f"{user.name} applied for the following job:\n{job_listing.display_details()}"

# Concrete subclass of Person for an employer
class Employer(user):
    def introduce(self):
        return f"Employer: {self.name}"

    @classmethod
    def interact(cls, person, job_listing):
        return f"{user.name} posted the following job:\n{job_listing.display_details()}"

# Class method to count the number of job listings
class CareerPortal:
    job_listings = []

    @classmethod
    def add_job_listing(cls, job):
        cls.job_listings.append(job)

    @classmethod
    def count_job_listings(cls):
        return len(cls.job_listings)

# Initialize the CareerPortal
career_portal = CareerPortal()

job1 = FullTimeJob("software Engineer","Mumbai","minimum 3 months experience",250000)
job2 = PartTimeJob("accountent","dilsuknagar","accountent job description","Daily 4hr{1500}")

CareerPortal.add_job_listing(job1)
CareerPortal.add_job_listing(job2)

while True:
    print("1. Post a job listing")
    print("2. Add a user")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        job_type = input("Enter job type (Full-Time or Part-Time): ")
        title = input("Enter job title: ")
        location = input("Enter job location: ")
        description = input("Enter job description: ")
        
        if job_type.lower() == "full-time":
            salary = int(input("Enter salary: "))
            job = FullTimeJob(title, location, description, salary)
            print(job.display_details())

        elif job_type.lower() == "part-time":
            work_per_week = int(input("Enter work per week: ""hrs"))
            job = PartTimeJob(title, location, description, work_per_week)
            print(job.display_details())

        else:
            print("Invalid job type. Please enter Full-Time or Part-Time.")
            continue

        CareerPortal.add_job_listing(job)
        print("Job listing added successfully!")

    elif choice == "2":
        user_type = input("Enter user type (Applicant or Employer): ")
        name = input("Enter user name: ")
        email = input("Enter user email: ")
    
        if user_type.lower() == "applicant":
            user = Applicant(career_portal, name, email)
            
        elif user_type.lower() == "employer":
            user = Employer(career_portal, name, email)
            
        else:
            print("Invalid user type. Please enter Applicant or Employer.")
            continue

        print(f"User {name} added successfully!")

    elif choice == "3":
        break

# Display the count of job listings
job_count = CareerPortal.count_job_listings()
Application_count = CareerPortal.applications()
print(f"Total job listings: {job_count}")
print(f"Total job applications: {Application_count}")
