const core = require('@actions/core');
const github = require('@actions/github');
const pattern = /^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\(\w+\))?((?=:\s)|(?=!:\s))?(!)?(:\s\_\_.*\_\_)($|( *\n\n)(.+)?(\n\n)((resolve[ds]? \#\d+|fix(ed|es)? \#\d+|close[ds]? \#\d+)(, )?)+$)/g;

const commits = JSON.parse(github.context.payload.event).commits;

if (commits.length >= 20) {
    core.setFailed("Pull request must contain fewer than 20 commits.");
} else {
    commits.every((commit) => {
        if (commit.author.name == 'actions-user' || pattern.test(commit.message)) {
            console.log(`VALID: ${commit.message}`)
            return true
        } else {
            core.setFailed(`INVALID: ${commit.message}`)
            return false
        }
    });
};
