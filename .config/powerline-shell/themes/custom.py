from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 7
    USERNAME_BG = 1
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 7
    HOSTNAME_BG = 2

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 2  # dark grey
    PATH_FG = 7  # light grey
    CWD_FG = 7  # white
    SEPARATOR_FG = 7

    READONLY_BG = 1
    READONLY_FG = 7

    REPO_CLEAN_BG = 3   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 7   # red
    REPO_DIRTY_FG = 88  # white

    GIT_AHEAD_BG = 240
    GIT_AHEAD_FG = 250
    GIT_BEHIND_BG = 240
    GIT_BEHIND_FG = 250
    GIT_STAGED_BG = 22
    GIT_STAGED_FG = 15
    GIT_NOTSTAGED_BG = 130
    GIT_NOTSTAGED_FG = 15
    GIT_UNTRACKED_BG = 89
    GIT_UNTRACKED_FG = 15
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = 15

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
