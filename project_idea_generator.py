import random

def generate_project_idea():
    """Generate a random coding project idea."""
    
    domains = [
        "Web Development", "Mobile App", "Data Science", "Machine Learning",
        "Game Development", "Automation", "IoT", "Blockchain", "AR/VR",
        "Desktop Application", "CLI Tool", "API Service"
    ]
    
    project_types = [
        "To-Do List", "Social Network", "E-commerce Platform", "Blog System",
        "Weather App", "Recipe Manager", "Expense Tracker", "Chat Application",
        "Portfolio Website", "Quiz Game", "Note Taking App", "File Converter",
        "Calendar App", "Music Player", "Password Manager", "Fitness Tracker"
    ]
    
    technologies = [
        "Python", "JavaScript", "React", "Node.js", "Flutter", "Django",
        "Vue.js", "Angular", "Swift", "Kotlin", "TensorFlow", "PyTorch",
        "Unity", "MongoDB", "PostgreSQL", "Firebase", "AWS", "Docker"
    ]
    
    features = [
        "user authentication", "real-time updates", "data visualization",
        "offline functionality", "cloud synchronization", "dark mode",
        "voice commands", "social sharing", "payment integration",
        "recommendation system", "multi-language support", "analytics dashboard"
    ]
    
    domain = random.choice(domains)
    project_type = random.choice(project_types)
    technology = random.choice(technologies)
    feature = random.choice(features)
    
    idea = f"Build a {project_type} using {technology} with {feature} for {domain}."
    return idea

def generate_multiple_ideas(count=5):
    """Generate multiple project ideas."""
    ideas = []
    for _ in range(count):
        ideas.append(generate_project_idea())
    return ideas

# Example usage
if __name__ == "__main__":
    print("🚀 CODING PROJECT IDEA GENERATOR 🚀")
    print("----------------------------------")
    
    # Generate a single idea
    print("\n🔍 Here's a project idea for you:")
    print(generate_project_idea())
    
    # Generate multiple ideas
    print("\n🔍 Need more inspiration? Here are 3 more ideas:")
    for i, idea in enumerate(generate_multiple_ideas(3), 1):
        print(f"{i}. {idea}")
    
    print("\nHappy coding! 💻")
