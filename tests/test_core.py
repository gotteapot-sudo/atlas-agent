from atlas import get_project_info


def test_get_project_info_returns_expected_metadata() -> None:
    project_info = get_project_info()

    assert isinstance(project_info, dict)
    assert project_info["name"] == "Atlas"
    assert project_info["version"]
    assert "development" in project_info["status"]
