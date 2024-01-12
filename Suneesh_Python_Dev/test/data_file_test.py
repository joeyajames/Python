# fixture_demo.py
import matplotlib.pyplot as plt
import pandas as pd
import pytest

from sj_pandas.sj_data_file import SJDataFile


@pytest.fixture
def example_fixture():
    file = SJDataFile('../resources/data.csv')
    return file.data


def test_with_fixture(example_fixture):
    val = example_fixture
    print(f"items = {val.items}")
    print(f"keys = {val.keys()}")
    print(f"to_dict = {val.to_dict('tight')}")

    val.plot()
    plt.show()

    print("Whole data frame = {%s}" % val)

    assert isinstance(val, pd.DataFrame)
