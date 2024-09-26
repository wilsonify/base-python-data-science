from io import StringIO

import matplotlib.pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0306_state_borders import (
    plot_state_borders,
    lines_to_segments
)

sample_state_lines = """
<state name ="Alabama" colour="#ff0000" >
  <point lat="35.0041" lng="-88.1955"/>
  <point lat="34.9918" lng="-85.6068"/>
  <point lat="32.8404" lng="-85.1756"/>
  <point lat="32.2593" lng="-84.8927"/>
  <point lat="32.1535" lng="-85.0342"/>
  <point lat="31.7947" lng="-85.1358"/>
  <point lat="31.5200" lng="-85.0438"/>
  <point lat="31.3384" lng="-85.0836"/>
  <point lat="31.2093" lng="-85.1070"/>
  <point lat="31.0023" lng="-84.9944"/>
  <point lat="30.9953" lng="-87.6009"/>
  <point lat="30.9423" lng="-87.5926"/>
  <point lat="30.8539" lng="-87.6256"/>
  <point lat="30.6745" lng="-87.4072"/>
  <point lat="30.4404" lng="-87.3688"/>
  <point lat="30.1463" lng="-87.5240"/>
  <point lat="30.1546" lng="-88.3864"/>
  <point lat="31.8939" lng="-88.4743"/>
  <point lat="34.8938" lng="-88.1021"/>
  <point lat="34.9479" lng="-88.1721"/>
  <point lat="34.9107" lng="-88.1461"/>
</state>
<state name ="Arkansas" colour="#ff0000" >
  <point lat="33.0225" lng="-94.0416"/>
  <point lat="33.0075" lng="-91.2057"/>
  <point lat="33.1180" lng="-91.1989"/>
  <point lat="33.1824" lng="-91.1041"/>
  <point lat="33.3053" lng="-91.1343"/>
  <point lat="33.4211" lng="-91.1646"/>
  <point lat="33.4337" lng="-91.2263"/>
  <point lat="33.5403" lng="-91.2524"/>
  <point lat="33.6112" lng="-91.1797"/>
  <point lat="33.6855" lng="-91.2524"/>
  <point lat="33.6946" lng="-91.1261"/>
  <point lat="33.7883" lng="-91.1412"/>
  <point lat="33.7700" lng="-91.0451"/>
  <point lat="33.8328" lng="-91.0341"/>
  <point lat="33.9399" lng="-91.0863"/>
  <point lat="34.0208" lng="-90.9256"/>
  <point lat="34.0856" lng="-90.9036"/>
  <point lat="34.1345" lng="-90.9586"/>
  <point lat="34.1675" lng="-90.9132"/>
  <point lat="34.1380" lng="-90.8501"/>
  <point lat="34.2311" lng="-90.9325"/>
  <point lat="34.3446" lng="-90.6935"/>
  <point lat="34.4409" lng="-90.5603"/>
  <point lat="34.5348" lng="-90.5548"/>
  <point lat="34.5959" lng="-90.5768"/>
  <point lat="34.7213" lng="-90.5301"/>
  <point lat="34.7574" lng="-90.5328"/>
  <point lat="34.8780" lng="-90.4546"/>
  <point lat="34.8454" lng="-90.3529"/>
  <point lat="34.8690" lng="-90.2911"/>
  <point lat="35.0255" lng="-90.3104"/>
  <point lat="35.1154" lng="-90.2843"/>
  <point lat="35.1323" lng="-90.1772"/>
  <point lat="35.1985" lng="-90.1112"/>
  <point lat="35.2826" lng="-90.1524"/>
  <point lat="35.4383" lng="-90.1332"/>
  <point lat="35.5579" lng="-90.0206"/>
  <point lat="35.6740" lng="-89.9780"/>
  <point lat="35.7287" lng="-89.9547"/>
  <point lat="35.9169" lng="-89.6594"/>
  <point lat="35.9658" lng="-89.6883"/>
  <point lat="36.0013" lng="-89.7130"/>
  <point lat="35.9958" lng="-90.3735"/>
  <point lat="36.1268" lng="-90.2664"/>
  <point lat="36.2875" lng="-90.0934"/>
  <point lat="36.3892" lng="-90.0742"/>
  <point lat="36.4180" lng="-90.1511"/>
  <point lat="36.4997" lng="-90.1566"/>
  <point lat="36.4986" lng="-94.6198"/>
  <point lat="35.3801" lng="-94.4412"/>
  <point lat="33.6318" lng="-94.4893"/>
  <point lat="33.6421" lng="-94.4522"/>
  <point lat="33.5597" lng="-94.4000"/>
  <point lat="33.5883" lng="-94.2462"/>
  <point lat="33.5872" lng="-94.1885"/>
  <point lat="33.5345" lng="-94.0375"/>
  <point lat="33.4314" lng="-94.0430"/>
  <point lat="33.0213" lng="-94.0430"/>
</state> 
"""


def test_lines_to_segments():
    """Test the lines_to_segments function for correct segment extraction."""
    segments = lines_to_segments(StringIO(sample_state_lines))

    # Check if the right number of segments are generated
    assert len(segments) == 77, "There should be two segments for two states."

    # Check that the segments match the expected values
    expected_segments = [
        ((-88.1955, 35.0041), (-85.6068, 34.9918)),
        ((-85.6068, 34.9918), (-85.1756, 32.8404)),
        ((-85.1756, 32.8404), (-84.8927, 32.2593)),
        ((-84.8927, 32.2593), (-85.0342, 32.1535)),
        ((-85.0342, 32.1535), (-85.1358, 31.7947)),
        ((-85.1358, 31.7947), (-85.0438, 31.52)),
        ((-85.0438, 31.52), (-85.0836, 31.3384)),
        ((-85.0836, 31.3384), (-85.107, 31.2093)),
        ((-85.107, 31.2093), (-84.9944, 31.0023)),
        ((-84.9944, 31.0023), (-87.6009, 30.9953)),
        ((-87.6009, 30.9953), (-87.5926, 30.9423)),
        ((-87.5926, 30.9423), (-87.6256, 30.8539)),
        ((-87.6256, 30.8539), (-87.4072, 30.6745)),
        ((-87.4072, 30.6745), (-87.3688, 30.4404)),
        ((-87.3688, 30.4404), (-87.524, 30.1463)),
        ((-87.524, 30.1463), (-88.3864, 30.1546)),
        ((-88.3864, 30.1546), (-88.4743, 31.8939)),
        ((-88.4743, 31.8939), (-88.1021, 34.8938)),
        ((-88.1021, 34.8938), (-88.1721, 34.9479)),
        ((-88.1721, 34.9479), (-88.1461, 34.9107)),
        ((-94.0416, 33.0225), (-91.2057, 33.0075)),
        ((-91.2057, 33.0075), (-91.1989, 33.118)),
        ((-91.1989, 33.118), (-91.1041, 33.1824)),
        ((-91.1041, 33.1824), (-91.1343, 33.3053)),
        ((-91.1343, 33.3053), (-91.1646, 33.4211)),
        ((-91.1646, 33.4211), (-91.2263, 33.4337)),
        ((-91.2263, 33.4337), (-91.2524, 33.5403)),
        ((-91.2524, 33.5403), (-91.1797, 33.6112)),
        ((-91.1797, 33.6112), (-91.2524, 33.6855)),
        ((-91.2524, 33.6855), (-91.1261, 33.6946)),
        ((-91.1261, 33.6946), (-91.1412, 33.7883)),
        ((-91.1412, 33.7883), (-91.0451, 33.77)),
        ((-91.0451, 33.77), (-91.0341, 33.8328)),
        ((-91.0341, 33.8328), (-91.0863, 33.9399)),
        ((-91.0863, 33.9399), (-90.9256, 34.0208)),
        ((-90.9256, 34.0208), (-90.9036, 34.0856)),
        ((-90.9036, 34.0856), (-90.9586, 34.1345)),
        ((-90.9586, 34.1345), (-90.9132, 34.1675)),
        ((-90.9132, 34.1675), (-90.8501, 34.138)),
        ((-90.8501, 34.138), (-90.9325, 34.2311)),
        ((-90.9325, 34.2311), (-90.6935, 34.3446)),
        ((-90.6935, 34.3446), (-90.5603, 34.4409)),
        ((-90.5603, 34.4409), (-90.5548, 34.5348)),
        ((-90.5548, 34.5348), (-90.5768, 34.5959)),
        ((-90.5768, 34.5959), (-90.5301, 34.7213)),
        ((-90.5301, 34.7213), (-90.5328, 34.7574)),
        ((-90.5328, 34.7574), (-90.4546, 34.878)),
        ((-90.4546, 34.878), (-90.3529, 34.8454)),
        ((-90.3529, 34.8454), (-90.2911, 34.869)),
        ((-90.2911, 34.869), (-90.3104, 35.0255)),
        ((-90.3104, 35.0255), (-90.2843, 35.1154)),
        ((-90.2843, 35.1154), (-90.1772, 35.1323)),
        ((-90.1772, 35.1323), (-90.1112, 35.1985)),
        ((-90.1112, 35.1985), (-90.1524, 35.2826)),
        ((-90.1524, 35.2826), (-90.1332, 35.4383)),
        ((-90.1332, 35.4383), (-90.0206, 35.5579)),
        ((-90.0206, 35.5579), (-89.978, 35.674)),
        ((-89.978, 35.674), (-89.9547, 35.7287)),
        ((-89.9547, 35.7287), (-89.6594, 35.9169)),
        ((-89.6594, 35.9169), (-89.6883, 35.9658)),
        ((-89.6883, 35.9658), (-89.713, 36.0013)),
        ((-89.713, 36.0013), (-90.3735, 35.9958)),
        ((-90.3735, 35.9958), (-90.2664, 36.1268)),
        ((-90.2664, 36.1268), (-90.0934, 36.2875)),
        ((-90.0934, 36.2875), (-90.0742, 36.3892)),
        ((-90.0742, 36.3892), (-90.1511, 36.418)),
        ((-90.1511, 36.418), (-90.1566, 36.4997)),
        ((-90.1566, 36.4997), (-94.6198, 36.4986)),
        ((-94.6198, 36.4986), (-94.4412, 35.3801)),
        ((-94.4412, 35.3801), (-94.4893, 33.6318)),
        ((-94.4893, 33.6318), (-94.4522, 33.6421)),
        ((-94.4522, 33.6421), (-94.4, 33.5597)),
        ((-94.4, 33.5597), (-94.2462, 33.5883)),
        ((-94.2462, 33.5883), (-94.1885, 33.5872)),
        ((-94.1885, 33.5872), (-94.0375, 33.5345)),
        ((-94.0375, 33.5345), (-94.043, 33.4314)),
        ((-94.043, 33.4314), (-94.043, 33.0213))]
    assert segments == expected_segments, "Segments should match expected coordinates."
    plt.close('all')


def test_plot_state_borders():
    """Test the plot_state_borders function."""
    # Call the function to test
    fig, ax = plot_state_borders(StringIO(sample_state_lines), color="0.8")

    # Check if a plot was created
    assert fig is not None, "Figure should not be None."
    assert len(ax.lines) > 0, "There should be lines on the plot."

    # Check if the correct number of lines were plotted
    assert len(ax.lines) == 77, "There should be two lines plotted for two state borders."

    # Check if the line color is correctly set
    for line in ax.lines:
        assert line.get_color() == "0.8", "Line color should be '0.8'."

    plt.close('all')
