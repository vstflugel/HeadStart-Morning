import os
import time
import json

class DailyThoughtsAndGoals:
    """Class containing rules, thought, goals, insights, reminders"""
    @staticmethod
    def joining_rules():
        """
        Joining Rules        
        """
        rules = {
                    "RULE #1": "An addiction to distraction is the end of your creative production. "
                                "Empire-makers and history-creators take one hour for themselves before "
                                "dawn, in the serenity that lies beyond the clutches of complexity, to "
                                "prepare themselves for a world-class day.",
                    
                    "RULE #2": "Excuses breed no genius. Just because you haven’t installed the early-rising habit "
                                "before doesn’t mean you can’t do it now. Release your rationalizations and remember "
                                "that small daily improvements, when done consistently over time, lead to stunning results.",
                    
                    "RULE #3": "All change is hard at first, messy in the middle and gorgeous at the end. "
                                "Everything you now find easy you first found difficult. With consistent practice, getting "
                                "up with the sun will become your new normal. And automatic.",
                    
                    "RULE #4": "To have the results The Top 5% of producers have, you must start doing what 95% of people "
                                "are unwilling to do. As you start to live like this, the majority will call you crazy. "
                                "Remember that being labeled a freak is the price of greatness.",
                    
                    "RULE #5": "When you feel like surrendering, continue. Triumph loves the relentless."
                }
        return rules

    @staticmethod
    def get_truths():
        """
        Truths        
        """
        truths = {
            "Truth #1": "World-class willpower is not something you are born with. It is developed through practice.",
            "Truth #2": "Personal discipline is like a muscle. The more you stretch it, the stronger it grows.",
            "Truth #3": "Like other muscles, willpower also weakens when it is tired. Recovery is, therefore, necessary.",
            "Truth #4": "There is always a four-step formula to install any great habit.",
            "Truth #5": "If you increase self-control in one area of your life, it will be automatically increased in all other areas too."
        }
        return truths

    @staticmethod
    def get_values():        # Define the 3 values of heroic habit-makers
        """
        Values        
        """
        values = {
            "Value #1": "You must be consistent and persistent if you want to win.",
            "Value #2": "Follow through with what you started to show personal respect.",
            "Value #3": "You will perform in public how you perform in private.",
            "Value #4": "Focus on listening more than you speak today.",
            "Value #5": "Ground yourself in your values throughout the day.",
        }
        return values


    @staticmethod
    def get_must_avoid():        # Define the 3 values of heroic habit-makers
        """
        Must Avoid        
        """
        # Define the 1 general theory of self-discipline Spartans
        must_avoid = {
                "Mistake #1" : "Leave Porn, Don't even think about any dirty stuffs, and no Mastrubation",
                "Mistake #2" : "No Sugar, No Processed Food, No Overacting or oversmartness",
                "Mistake #3" : "No wasting your Time/Energy, Save your time and Energy as much as possible.",
                "Mistake #4" : "Don't MULTI-TASK, channelize my ENERGY and TIME and build FOCUS",
                }
        return must_avoid

    @staticmethod
    def get_day_planner_commands():        # define the 3 values of heroic habit-makers
        """
        Day Planner
        """
        # define the 1 general theory of self-discipline spartans
        theory = [
                "Did the set your phone on dnd ?",
                "Did you created the top 3 task for today ?",
                "Did you created the won't do list for today ?",
                "Focus on listening more than you speak today.",
                #"Don't forget to meet 3 new people today.",
                # "Are you ready for 60/10 rule ?",
                ]
        return theory

    @staticmethod
    def get_2x3x_mindset():
        """
        The 2x3x mindset values.
        """
        values = {
            "Warrior's Mindset" : "Warriors do things that are hard but also important. So they do it regularly.",
            "Mindset Principle": "Triple your investment in personal mastery and professional capability to double your income and impact.",
            "Personal Growth": "It’s good for your personal growth. You attract what you are.",
            "Knowledge Value": "The more knowledge you have, the more valuable you become.",
            "Life Philosophy": "You’ll receive from life what you’ll give to it."
        }
        return values

    @staticmethod
    def habit_building_phases():
        """
        Phases of building a new habit.
        """
        phases = {
            "Destruction Phase": "22 days - Destruction of old habits.",
            "Installation Phase": "22 days - Installation of new habits.",
            "Integration Phase": "22 days - Integration of new habits.",
            "Total Duration": "66 days to build a new habit."
        }
        return phases

    @staticmethod
    def genius_assets():
        """
       'The 5 Assets of Genius.'
        """
        assets = {
            "Asset #1": "Mental focus",
            "Asset #2": "Physical energy",
            "Asset #3": "Willpower",
            "Asset #4": "Original talent",
            "Asset #5": "Daily time"
        }
        return assets

    @staticmethod
    def performance_cycles():
        """
        Define the two cycles of elite performance.
        """
        cycles = {
            "High Excellence Cycle (HEC)": "The period of passionate and focused work.",
            "Deep Refueling Cycle (DRC)": "The period of relaxation and fun."
        }
        return cycles

    @staticmethod
    def productivity_rules():
        """
       The two cycles of elite performance.
        """
        cycles = {
            "Refueling Cycle":"Take regular breaks and naps during the day to maintain focus.",
            "Deep Refueling Cycle (DRC)": "The period of relaxation and fun."
        }
        return cycles


    @staticmethod
    def leadership_core_values():
        """
        My Core Values of leadership 
        """
        core_values = {
            "Integrity & Accountability": "High standards, honesty, and reliability. Belief: Do the right thing, always.",
            "Excellence & Mastery": "Results-driven, goal-focused, no tolerance for mediocrity. Belief: Progress and precision are non-negotiable.",
            "Efficiency & Time Optimization": "Value productivity and eliminating waste. Belief: Time is precious; respect it.",
            "Growth & Innovation": "Embrace progress, creativity, and challenging the status quo. Belief: Standing still = falling behind.",
            "Autonomy & Self-Sufficiency": "Empower others, avoid micromanagement. Belief: Leaders create leaders."
        }
        return core_values



    @staticmethod
    def no_quotes():
        """
        Power of saying 'No'.
        """
        quotes = {
            "Say No to Almost Everything": "The difference between successful people and really successful people is that really successful people say no to almost everything. – Warren Buffett",
            "What You Don't Do Matters": "What you don't do determines what you can do. – Tim Ferriss",
            "Assertive Repetition": "If the person continues to ask you, even after you've said no, you can simply repeat your last statement in a calm voice. You would repeat the same language every time they ask. Stay firm while being polite and professional.",
            "'No' is a Complete Sentence": "'No' is a complete sentence. You do not owe anyone a detailed explanation of why you say no.",
            "Focus and innovation is Saying No": "Focus is about saying no. Innovation is saying no to 1,000 things. – Steve Jobs",
            "Say No to Distractions": "You can’t let praise or criticism get to you. It’s a weakness to get caught up in either one. – John Wooden (on saying no to distractions)",
            "No Protects Your Energy": "'No' is a powerful word. It protects your time, energy, and focus—the foundations of leadership."
        }
        return quotes


    @staticmethod
    def focus_principles():
        """
        Focus Principles
        """
        principles = {
            "Deep Work is a Superpower": "Deep work is a habit, not a talent. Prioritize depth over shallow busyness to unlock creativity and productivity.",
            "Deep Refueling Cycle": "Take regular breaks and naps during the day to maintain focus.",
            "Clarity Drives Results": "Your scattered focus results in a scattered life. Clarity breeds success—know your priorities.",
            "Tackle the Hardest First (Eat the Frog)": "Eat the ugliest frog first: Tackle your most challenging/important task (MIT) first every morning.",
            "Single-Tasking Mastery": "Practice single-tasking: Dedicate 25-minute blocks (Pomodoro Technique) to one task. Turn off notifications, close tabs, and resist multitasking.",
            "80/20 Focus": "Apply the 80/20 Rule: Focus 80% of your effort on the 20% of tasks that deliver 80% of results.",
            "Creative Procrastination": "Delay or ignore non-essential tasks guilt-free. Focus only on what truly matters.",

        }
        return principles


    @staticmethod
    def mindfulness_practices():
        """
        Mindfulness Practices to cultivate Presence and Enhance Clarity.
        """
        practices = {
            "Breath Awareness Anchor": "Use your breath as an anchor. When distracted, pause, take 3 deep breaths, and refocus. Example: Before starting a task, close your eyes for 30 seconds and focus on your inhale/exhale.",
            "Mindful Listening": "Practice mindful communication: Listen actively. When someone speaks, focus 100% on their words, tone, and body language—not your response.",
            "Label Emotions": "Reduce emotional reactivity: When stressed, pause and name the emotion (e.g., 'I’m feeling anxious because…'). Naming creates distance and restores clarity.",
            "Embrace Boredom & Deep Work": "Schedule boredom periods and deep work blocks. Train your mind to resist the urge for constant stimulation during these moments.",
        }
        return practices

