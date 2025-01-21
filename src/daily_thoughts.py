import os
import time
import json

class DailyThoughtsAndGoals:
    """Class containing rules, thought, goals, insights, reminders"""
    @staticmethod
    def joining_rules():
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
        values = {
            "Value #1": "You must be consistent and persistent if you want to win.",
            "Value #2": "Follow through with what you started to show personal respect.",
            "Value #3": "You will perform in public how you perform in private."
        }
        return values


    @staticmethod
    def get_must_avoid():        # Define the 3 values of heroic habit-makers
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
        # define the 1 general theory of self-discipline spartans
        theory = [
                 "did the set your phone on dnd ?",
                 "did you created the top 3 task for today ?",
                 "don't forget to meet 3 new people today.",
                 "are you ready for 60/10 rule ?",
                ]
        return theory

    @staticmethod
    def get_2x3x_mindset():
        """
        Define the 2x3x mindset values.
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
        Define the phases of building a new habit.
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
        Define 'The 5 Assets of Genius.'
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
