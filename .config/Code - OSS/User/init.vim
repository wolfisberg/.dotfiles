" Keybinds to set in the IDE
"   <C-H> => <Left>
"   <C-J> => <Down>
"   <C-K> => <Up>
"   <C-L> => <Right>

" Improvements
"   <C-N>/<C-P> don't work in structure popup when filtered

let mapleader = "\<Space>"

" GENERAL
set visualbell
set noerrorbells
set relativenumber
set number
set scrolloff=8

" SEARCH
set showmatch
set nohlsearch
set ignorecase
set smartcase
set incsearch
nmap <leader>h       :noh<CR>

" NAVIGATION
" todo nmap <C-S-l>         <C-W>l
" todo nmap <C-S-h>         <C-W>h

" SPLITS/TABS
set splitbelow
set splitright

" CODE NAVIGATION
nmap <leader>o       <Cmd>call VSCodeNotify('workbench.action.gotoSymbol')<CR>
nmap <leader>gd      <Cmd>call VSCodeNotify('editor.action.revealDefinition')<CR>
nmap <leader>gt      <Cmd>call VSCodeNotify('editor.action.goToTypeDefinition')<CR>
nmap <leader>gu      <Cmd>call VSCodeNotify('editor.action.goToReferences')<CR>
nmap <leader>gU      <Cmd>call VSCodeNotify('references-view.findReferences')<CR>
nmap <leader>gi      <Cmd>call VSCodeNotify('editor.action.goToImplementation')<CR>
nmap g;              <Cmd>call VSCodeNotify('workbench.action.navigateBackInEditLocations')<CR>
nmap g,              <Cmd>call VSCodeNotify('workbench.action.navigateForwardInEditLocations')<CR>
" todo nmap <F2>            <Action>(GotoNextError)
" todo nmap <F14>           <Action>(GotoPreviousError)

" QUICK PREVIEWS
nmap <leader>qd      <Cmd>call VSCodeNotify('editor.action.peekDefinition')<CR>
nmap <leader>qi      <Cmd>call VSCodeNotify('editor.action.peekImplementation')<CR>
nmap <leader>qt      <Cmd>call VSCodeNotify('editor.action.peekTypeDefinition')<CR>
" todo nmap <leader>qe      <Action>(ShowErrorDescription)
" todo nmap <leader>qb      <Action>(ShowBookmarks)

" REFACTORING
" todo nmap <leader>rm      <Action>(Refactorings.QuickListPopupAction)
" todo nmap <leader>rn      <Action>(RefactoringMenu)
nmap <leader>rr      <Cmd>call VSCodeNotify('editor.action.rename')<CR>

" PROJECT NAVIGATION
nmap <leader>fe      <Cmd>call VSCodeNotify('workbench.action.findInFiles')<CR>
nmap <leader>fa      <Cmd>call VSCodeNotify('workbench.action.showCommands')<CR>
nmap <leader>ff      <Cmd>call VSCodeNotify('workbench.action.quickOpen')<CR>
nmap <leader>fs      <Cmd>call VSCodeNotify('workbench.action.showAllSymbols')<CR>
nmap <leader>fr      <Cmd>call VSCodeNotify('workbench.action.showAllEditorsByMostRecentlyUsed')<CR>
" todo nmap <leader>fR      <Action>(RecentChangedFiles)
" todo nmap <leader>fl      <Action>(RecentLocations)

" TOOL WINDOWS
" todo nmap <leader>wh      <Action>(HideAllWindows)
nmap <leader>wP      <Cmd>call VSCodeNotify('workbench.view.explorer')<CR>
nmap <leader>wp      <Cmd>call VSCodeNotify('workbench.files.action.showActiveFileInExplorer')<CR>
nmap <leader>wd      <Cmd>call VSCodeNotify('workbench.view.debug')<CR>
" todo nmap <leader>wr      <Action>(ActivateRunToolWindow)
nmap <leader>wt      <Cmd>call VSCodeNotify('workbench.view.extension.todo-tree-container')<CR>
nmap <leader>wf      <Cmd>call VSCodeNotify('workbench.view.search')<CR>
" todo nmap <leader>wy      <Action>(ActivatePythonConsoleToolWindow)
" todo nmap <leader>wl      <Action>(JumpToLastWindow)
" todo nmap <leader>m       <Action>(QuickJavaDoc)

" DEBUGGING
nmap <leader>ds      <Cmd>call VSCodeNotify('workbench.action.debug.stop')<CR>
nmap <leader>dd      <Cmd>call VSCodeNotify('workbench.action.debug.start')<CR>
nmap <leader>dr      <Cmd>call VSCodeNotify('workbench.action.debug.run')<CR>
nmap <leader>dcd     <Cmd>call VSCodeNotify('workbench.action.debug.selectandstart')<CR>
" todo nmap <leader>dcr     <Action>(ChooseRunConfiguration)
nmap <leader>de      <Cmd>call VSCodeNotify('workbench.debug.action.toggleRepl')<CR>

nmap <leader>db      <Cmd>call VSCodeNotify('editor.debug.action.toggleBreakpoint')<CR>
" todo toggle breakpoint nmap <leader>dt      <Cmd>call VSCodeNotify('')<CR>
nmap <leader>dB      <Cmd>call VSCodeNotify('workbench.debug.action.focusBreakpointsView')<CR>

" todo nmap <leader>dx      <Action>(ShowExecutionPoint)
" todo nmap <leader>di      <Action>(Debugger.EvaluateInConsole)<Action>(NavigateToImmediateWindow)
