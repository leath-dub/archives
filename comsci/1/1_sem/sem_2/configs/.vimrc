set nu
syntax on
set smartindent
set shiftwidth=4
set tabstop=4
set expandtab
set scrolloff=10
set nowrap
set incsearch
set ignorecase
set smartcase
set showcmd
set hlsearch
set wildmenu
set wildmode=list:longest
set wildignore=*.docx,*.jpg,*.png,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set backspace=indent,eol,start

call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'JamshedVesuna/vim-markdown-preview'

call plug#end()

colorscheme gruvbox
set background=dark
let vim_markdown_preview_github=1
