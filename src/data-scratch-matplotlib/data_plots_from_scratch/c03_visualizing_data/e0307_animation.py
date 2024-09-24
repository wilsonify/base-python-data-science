from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
from matplotlib.gridspec import GridSpec


class LineTracker:
    def __init__(self, title, ylabel):
        self.artists_list = []
        self.fig = plt.figure(figsize=(8, 5))
        self.gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
        self.ax0 = self.fig.add_subplot(self.gs[0])
        self.line = self.ax0.plot([], [], color="green", marker="o", linestyle="solid")
        self.ax0.set_title(title)
        self.ax0.set_ylabel(ylabel)
        self.fig.tight_layout()

    def create_plot(self, x, y, output_path):
        self.ax0.plot(x, y, color="green", marker="o", linestyle="solid")
        plt.savefig(output_path)

    def update_plot(self, x, y):
        """
        Update the plot with new data.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the current frame of hurricane data.
        """
        self.scat = self.ax0.scatter(x, y)
        self.line, = self.ax0.plot(x, y, linestyle='-', color='blue')
        self.artists_list.append([self.scat, self.line])

    def animate(self, x, y, output_path):
        """
        Create an animation of the hurricane data.

        Parameters:
        df (pd.DataFrame): The DataFrame containing hurricane data.
        output_path (str): The path to save the animation.
        """
        for frame in range(len(x)):
            current_x = x[:frame + 1]
            current_y = y[:frame + 1]
            self.update_plot(current_x, current_y)
        anim = ArtistAnimation(self.fig, self.artists_list, interval=200, blit=True)
        anim.save(output_path)


if __name__ == "__main__":
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    lt = LineTracker(title="Nominal GDP", ylabel="Billions of $")
    lt.create_plot(x=years, y=gdp, output_path="e030701_simple_line_chart.png")

    lt = LineTracker(title="Nominal GDP", ylabel="Billions of $")
    lt.animate(x=years, y=gdp, output_path="e030702_animated_line_chart.gif")
