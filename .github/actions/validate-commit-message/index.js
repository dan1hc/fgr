const core = require("@actions/core");
const github = require("@actions/github");

const pattern = /^(Merge .*)|^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\(\w+\))?((?=:\s)|(?=!:\s))?(!)?(:\s\_\_.*\_\_)($|( *\n\n)(.+)?(\n\n)((resolve[ds]? \#\d+|fix(ed|es)? \#\d+|close[ds]? \#\d+)(, )?)+$)/;
const restClient = github.getOctokit(core.getInput('token'));

restClient.rest.pulls.listCommits(
    {
        owner: "dan1hc",
        repo: "fgr",
        per_page: 100,
        pull_number: github.context.payload.pull_request.number
        }
    ).then((response) => {
        if (response.data.length >= 100) {
            core.setFailed("Pull request must contain fewer than 100 commits.");
        } else {
            response.data.every((record) => {
                var commit = record.commit;
                console.log(`COMMITTER: ${commit.committer.name}`);
                console.log(`MESSAGE: ${commit.message}`);
                if (
                    commit.committer.name == "GitHub"
                    || commit.committer.name == "github-actions"
                    || pattern.test(commit.message)
                    ) {
                    console.log("VALID");
                    console.log("");
                    return true
                } else {
                    core.setFailed(`INVALID: ${commit.message}`);
                    return false
                };
            });
        };
    }, (error) => {
        core.setFailed(error);
        }
    );
