alias untracked_="git ls-files -o --directory --exclude-standard"
alias untracked="git ls-files -o --directory --exclude-standard | sed q1 > /dev/null"

unset PYTHONBREAKPOINT
alias pytest='pytest --pdbcls=IPython.core.debugger:Pdb'
alias htest='pytest -sx --no-cov --quiet --failed-first --tb=no --dist=no'
alias htestnox='pytest -s --no-cov --quiet --failed-first --tb=no'
alias htestv='pytest -sx --no-cov --failed-first'
alias htestcov='pytest --tb=no -n auto -qq'
alias htestfuzz='pytest --no-cov -n auto --runfuzz'

alias htoxtest='tox --develop -e py311-flake8_6'
alias htoxall='tox --develop -qp'


alias hcheck='untracked && git add -u && pre-commit run --show-diff-on-failure'
alias gfpush='untracked && pytest --quiet -x && git commit -a --amend --no-edit && git push --force-with-lease'

export LIBCST_PARSER_TYPE="native"
