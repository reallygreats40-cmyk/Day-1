class Report:
    def __init__(self, title):
        self.title = title

early = Report("Q1")            # created BEFORE the method exists

def summary(self):
    return f"Report {self.title} is ready"

# Attach the plain function to the class
Report.summary = summary

print(early.summary())          # Report Q1 is ready
print(Report("Q2").summary())   # Report Q2 is ready
