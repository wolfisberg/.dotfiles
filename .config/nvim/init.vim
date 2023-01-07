" VUNDLE
set nocompatible                            " be iMproved, required
filetype off                                " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'folke/tokyonight.nvim'
Plugin 'chrisbra/Colorizer'
Plugin 'tpope/vim-surround'
Plugin 'tpope/vim-commentary'
Plugin 'junegunn/fzf.vim'
Plugin 'antoinemadec/FixCursorHold.nvim'    " Dependency of fern.vim
Plugin 'lambdalisue/fern.vim'
Plugin 'lambdalisue/fern-hijack.vim'
Plugin 'lambdalisue/nerdfont.vim'
Plugin 'lambdalisue/fern-renderer-nerdfont.vim'
Plugin 'iamcco/markdown-preview.nvim'       " Dependency: yarn
Plugin 'neovim/nvim-lspconfig'
Plugin 'kabouzeid/nvim-lspinstall'
Plugin 'nvim-lua/completion-nvim'
Plugin 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
call vundle#end()                           " required
filetype plugin indent on                   " required
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ


" GENERAL
syntax on
autocmd VimEnter * hi Normal ctermbg=none

" THEME
lua << EOF
require("tokyonight").setup({
  style = "night", -- `storm`, `moon`, `night`, `day`
  transparent = true, -- Enable this to disable setting the background color
})
EOF

set noerrorbells
set number
set relativenumber
set scrolloff=8
set hidden

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab
set smartindent
set foldenable
set foldmethod=indent
set foldnestmax=5
set nofoldenable
set foldlevel=2
set nowrap

set nohlsearch
set showmatch
set ignorecase
set smartcase
set incsearch

let mapleader = " "
map <leader>h :noh<CR> 
map <C-c> "+y
map <C-p> "+P

" NAVIGATION
nnoremap <C-D> <S-M><C-D>
nnoremap <C-U> <S-M><C-U>

" SPLITS
set splitbelow
set splitright
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" COLORIZING
let g:colorizer_auto_filetype='rasi,lua,css,html,sh,vim,bash'

" LSP CONFIG / INSTALL / COMPLETE
set completeopt=menuone,noinsert
set shortmess+=c " Avoid showing extra message when using completion
let g:completion_matching_strategy_list = ['exact', 'substring', 'fuzzy']
let g:completion_matching_smart_case = 1
let g:completion_enable_auto_popup = 1
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

"lua << EOF
"local lsp_conf = require('lspconfig')
"local lsp_inst = require('lspinstall')
"
"local function setup_servers()
  "lsp_inst.setup()
  "for _, server in pairs(lsp_inst.installed_servers()) do
    "lsp_conf[server].setup { on_attach = require'completion'.on_attach }
  "end
"end
"
"setup_servers()
"
"require'lspinstall'.post_install_hook = function ()
  "setup_servers() -- reload installed servers
  "vim.cmd("bufdo e") -- this triggers the FileType autocmd that starts the server
"end
"EOF

" COMMENTER
nnoremap <leader>/ :Commentary<CR>
vnoremap <leader>/ :Commentary<CR>

" FZF
set rtp+=/usr/bin/fzf
let g:fzf_action = {'ctrl-t': 'tab split', 'ctrl-s': 'split', 'ctrl-v': 'vsplit'}
nnoremap <leader>ff :call fzf#run(fzf#wrap({
    \ 'source': 'fd --ignore-file "$HOME/.config/fd/.fdignore" . .'}))<CR>
nnoremap <leader>fh :call fzf#run(fzf#wrap({
    \ 'source': 'fd --hidden --ignore-file "$HOME/.config/fd/.fdignore" . "$HOME"'}))<CR>
nnoremap <leader>fb :call fzf#vim#buffers()<CR>

" FERN 
let g:fern#renderer = "nerdfont"
let g:fern#disable_default_mappings   = 1
let g:fern#disable_viewer_hide_cursor = 1
nnoremap <silent> <Leader>d :Fern . -drawer -width=40 -toggle -reveal=%<CR><C-w>=

function! FernInit() abort
    nmap <buffer> ? <Plug>(fern-action-help)
    nmap <buffer> <C-C> <Plug>(fern-action-cancel)
    nmap <buffer> <F5> <Plug>(fern-action-reload)

    nmap <buffer> h <Plug>(fern-action-collapse)
    "nmap <buffer> l <Plug>(fern-action-open-or-expand)
    nmap <buffer> <nowait> < <Plug>(fern-action-leave)
    nmap <buffer> <nowait> > <Plug>(fern-action-cd)<Plug>(fern-action-enter)
    nmap <buffer> zh <Plug>(fern-action-hidden:toggle)
    nmap <buffer> F <Plug>(fern-action-grep)

    nmap <buffer> s <Plug>(fern-action-open:split)
    nmap <buffer> v <Plug>(fern-action-open:vsplit)
    nmap <buffer> t <Plug>(fern-action-open:tabedit)
    nmap <buffer> S <Plug>(fern-action-open:system)

    nmap <buffer> M <Plug>(fern-action-clipboard-move)
    nmap <buffer> C <Plug>(fern-action-clipboard-copy)
    nmap <buffer> P <Plug>(fern-action-clipboard-paste)

    nmap <buffer> cp <Plug>(fern-action-copy)
    nmap <buffer> mv <Plug>(fern-action-move)
    nmap <buffer> rn <Plug>(fern-action-rename)
    nmap <buffer> rm <Plug>(fern-action-remove)
    nmap <buffer> mf <Plug>(fern-action-new-file)
    nmap <buffer> md <Plug>(fern-action-new-dir)

    nmap <buffer> x <Plug>(fern-action-mark:toggle)

    nmap <buffer><expr>
        \ <Plug>(fern-my-preview-or-nop)
        \ fern#smart#leaf(
        \   "\<Plug>(fern-action-open:edit)\<C-w>p",
        \   "",
        \ )
    nmap <buffer> w <Plug>(fern-my-preview-or-nop)


    nnoremap <Plug>(fern-close-drawer) :<C-U>FernDo close -drawer -stay<CR>
    nmap <buffer><silent><Plug>(fern-action-open-and-close)
        \ <Plug>(fern-action-open)
        \ <Plug>(fern-close-drawer)
    nmap <buffer><expr>
        \ <Plug>(fern-my-open-and-close-or-expand)
        \ fern#smart#leaf(
        \   "\<Plug>(fern-action-open-and-close)",
        \   "\<Plug>(fern-action-expand)",
        \ )
    nmap <buffer> l <Plug>(fern-my-open-and-close-or-expand)
endfunction

augroup FernEvents
    autocmd!
    autocmd FileType fern call FernInit()
augroup END

" MARKDOWN PREVIEW
nmap <leader>mp <Plug>MarkdownPreviewToggle

