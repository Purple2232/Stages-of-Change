import streamlit as st

# App title and introduction
st.title("Supporting Your Health with Screen and Light Use")
st.write("""
This tool helps you understand your relationship with screen use and artificial light and provides helpful suggestions based on your current readiness to manage potential health impacts. Our goal is to offer gentle support with practical, attainable resources.
""")

# Preliminary Questions to Assess Stage of Readiness
st.header("Assess Your Awareness and Readiness")
st.write("Answer the following questions to help us understand where you currently are in managing health impacts related to artificial light and screen use.")

# Question 1: Awareness of Health Impacts
awareness = st.radio("How familiar are you with potential health impacts of prolonged screen and light use?",
                     options=["Not familiar", "Somewhat familiar", "Quite familiar"])

# Question 2: Desire to Learn or Take Action
desire = st.radio("How interested are you in learning more or taking steps to mitigate any health impacts?",
                  options=["Not interested", "Considering it", "Would like to but unsure how", "Actively taking steps"])

# Question 3: Actions Taken
actions_taken = st.radio("Have you already taken any steps to reduce potential health impacts of screen and light use?",
                         options=["None", "Thinking about it", "Some steps", "Consistent changes"])

# Determine Stage and Provide Feedback
st.header("Your Readiness Stage and Personalized Support")

# Map responses to a stage of readiness
if awareness == "Not familiar" and desire == "Not interested":
    stage = "New to the Topic"
    st.subheader("Stage: New to the Topic")
    st.write("""
    It seems you're new to the topic of managing health impacts from screen and light exposure. Here’s some initial information to get started:
    """)
    st.markdown("""
    - **Health Effects**: Prolonged exposure to screens and artificial light can impact sleep, cause eye strain, and contribute to headaches and fatigue.
    - **Simple Tips**:
        - **Eye Breaks**: Follow the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds.
        - **Movement Breaks**: Get up and move for a minute every hour.
        - **Natural Light**: Try to spend a few minutes outside each day to balance screen time.
    - **Resources**:
        - [National Sleep Foundation](https://www.sleepfoundation.org)
        - [American Optometric Association](https://www.aoa.org)
    """)

elif awareness == "Somewhat familiar" and (desire in ["Considering it", "Would like to but unsure how"]):
    stage = "Curious but Unsure"
    st.subheader("Stage: Curious but Unsure")
    st.write("""
    You're curious about managing screen use but may not know where to begin. Here are some starting points:
    """)
    st.markdown("""
    - **Easy Adjustments**:
        - **Night Mode or Blue Light Filters**: Use these on devices to reduce eye strain.
        - **Reduce Evening Screen Time**: Limiting screen use 30 minutes before bed may improve sleep quality.
        - **Screen-Free Breaks**: Try setting regular breaks during long screen sessions.
    - **Resources**:
        - [Flux (Blue Light Filter)](https://justgetflux.com)
        - [Guided Eye Exercises](https://www.allaboutvision.com/conditions/eye-exercises/)
    """)

elif awareness == "Quite familiar" and desire == "Would like to but unsure how":
    stage = "Aware but Seeking Guidance"
    st.subheader("Stage: Aware but Seeking Guidance")
    st.write("""
    You’re aware of the potential health impacts of screen use and want to make changes but may need some guidance. Here are tailored tips:
    """)
    st.markdown("""
    - **Strategies to Implement**:
        - **Blue Light Glasses**: Consider using these if you often work or study at night.
        - **Lighting Adjustments**: Opt for softer lighting in the evening or use red lights to minimize eye strain.
        - **Break Scheduling**: Use a timer to remind yourself to take short, frequent breaks.
    - **Resources**:
        - [Zenni Blue Light Glasses](https://www.zennioptical.com/b/blue-light-glasses)
        - [Light Therapy Guide](https://www.sleepfoundation.org/circadian-rhythm/light-therapy)
    """)

elif awareness == "Quite familiar" and desire == "Actively taking steps" and actions_taken in ["Some steps", "Consistent changes"]:
    stage = "Taking Positive Steps"
    st.subheader("Stage: Taking Positive Steps")
    st.write("""
    You’re already taking proactive steps to balance your screen use and could benefit from further guidance to optimize your habits:
    """)
    st.markdown("""
    - **Tips for Refinement**:
        - **Regular Physical Movement**: Try adding stretches or brief walks to your routine every hour.
        - **Eye Exercises**: Explore targeted exercises to reduce eye strain, such as focusing on distant objects or figure-8 exercises.
        - **Ambient Lighting**: Use warm lights in the evening and maximize daylight exposure in the morning.
    - **Resources**:
        - [American Academy of Ophthalmology Eye Exercises](https://www.aao.org/eye-health/tips-prevention/computer-usage)
        - [Philips Hue Adjustable Lighting](https://www.philips-hue.com)
    """)

elif awareness == "Quite familiar" and actions_taken == "Consistent changes" and desire == "Actively taking steps":
    stage = "Balanced and Knowledgeable"
    st.subheader("Stage: Balanced and Knowledgeable")
    st.write("""
    You’re well-informed and have developed sustainable habits to balance screen use. Here are some advanced tips to help maintain your progress:
    """)
    st.markdown("""
    - **Additional Strategies**:
        - **Mindfulness Breaks**: Incorporate mindfulness or meditation during screen breaks for enhanced relaxation.
        - **Advanced Lighting Control**: Use smart lighting systems that mimic natural daylight cycles.
        - **Regular Assessments**: Periodically assess your screen use habits to maintain a balanced approach.
    - **Resources**:
        - [Calm Meditation App](https://www.calm.com)
        - [Lightmeter App for Tracking Brightness](https://lightmeter.app)
    """)

# Display the stage result and message
st.write(f"Based on your responses, you are in the **{stage}** stage.")
st.write("Remember, any small step towards balancing screen and light use can make a positive impact on your well-being. We’re here to support you in a way that fits into your lifestyle.")

# Closing statement
st.write("""
Thank you for exploring ways to manage your screen and light use healthfully. We hope these resources empower you to make choices that support your goals without unnecessary disruption or expense.
""")
