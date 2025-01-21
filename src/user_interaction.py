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

    def display_content_set(self, content):

        console.clear()
        console.rule("[bold blue]Motivational Rules")

        # Iterating through the content (which is a dictionary)
        for key, value in content.items():
            console.print(f"{key}:\n {value}", style="bold green")
            console.print()

        console.rule()
        console.input("\nPress Enter to exit...")


    def display_insights(self):
        """Get insights and thoughts for the morning"""

        rules = self.daily_thoughts.joining_rules()
        self.display_content_set(rules)

        truths = self.daily_thoughts.get_truths()
        self.display_content_set(truths)

        values = self.daily_thoughts.get_values()
        self.display_content_set(values)

        insights = self.daily_thoughts.get_2x3x_mindset()
        self.display_content_set(insights)

        content = self.daily_thoughts.habit_building_phases()
        self.display_content_set(content)

        content = self.daily_thoughts.get_must_avoid()
        self.display_content_set(content)

        content = self.daily_thoughts.genius_assets()
        self.display_content_set(content)

        content = self.daily_thoughts.performance_cycles()
        self.display_content_set(content)


        commands = self.daily_thoughts.get_day_planner_commands()
        self.display_commands_prompts(commands)
