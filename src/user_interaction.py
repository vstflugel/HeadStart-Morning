from daily_thoughts import DailyThoughtsAndGoals
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

# Initialize console for CLI-based UI
console = Console()

class UserInteraction:
    """Class to handle user interactions."""
    def __init__(self):

        console = Console()
        console.clear()
        self.daily_thoughts = DailyThoughtsAndGoals

        # Handling the execution flow of user interaction.
        self.display_insights()


    def display_commands_prompts(self, commands):
        console.clear()

        for i in range(len(commands)):
            # Create a centered, styled panel for the command
            panel = Panel(
                    Align.center(f"[bold yellow]{commands[i]}[/bold yellow]", vertical="middle"),
                    border_style="bold green",
                    padding=(2, 4),  # Adds spacing for better aesthetics
                    title="[bold blue]Command[/bold blue]",
                    title_align="center"
                    )

            # Display the panel
            console.print(panel, justify="center")

            # Wait for user input to move to the next command
            console.input("\nPress Enter for the next command...")

    def display_content_list(self, content):

        console.clear()
        console.rule("[bold blue]")

        # Iterating through the content (which is a dictionary)
        for i in range(len(content)):
            console.print(f"{i+1}:\n {content[i]}", style="bold green")
            console.print()

        console.rule()
        console.input("\nPress Enter to exit...")

    def display_content_set(self, content, title):

        console.clear()
        #console.rule(f"[bold blue]Motivational Rules")
        console.rule(f"[bold blue]{title}")

        # Iterating through the content (which is a dictionary)
        for key, value in content.items():
            console.print(f"{key}:\n {value}", style="bold green")
            console.print()

        console.rule()
        console.input("\nPress Enter to exit...")


    def display_insights(self):
        """Get insights and thoughts for the morning"""

        methods = [
            'joining_rules',
            'no_quotes',
            'focus_principles',
            'mindfulness_practices',
            'genius_assets',
            'leadership_core_values',
            'get_truths',
            'get_values',
            'get_2x3x_mindset',
            'habit_building_phases',
            'get_must_avoid',
            #'performance_cycles',
        ]

        for method_name in methods:
            method = getattr(self.daily_thoughts, method_name)
            docstring = method.__doc__.strip() if method.__doc__ else 'No description available'
            content = method()
            self.display_content_set(content, docstring)



        commands = self.daily_thoughts.get_day_planner_commands()
        self.display_commands_prompts(commands)
