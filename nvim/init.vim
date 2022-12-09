map ,d :NERDTreeToggle<cr>
map ,r :te make run<cr>:norm G<cr>
map ,cr :te make clean run<cr>:norm G<cr>
map ,f :call CreateFile()<cr>
map ,n :set number!<cr>

function! CreateFile()
    let path = input("Create file: ", expand("%:p:h").."/", "file")
    execute "!mkdir -p " .. fnamemodify(path, ":p:h")
    execute "!touch " .. fnamemodify(path, ":p")
    call feedkeys("<cr>")
    echo "Created " .. fnamemodify(path, ":t")
endfunction

" Coc
map gd <Plug>(coc-definition)
map gi <Plug>(coc-implementation)
map gr <Plug>(coc-references)
inoremap <expr> <cr> coc#pum#visible() ? coc#pum#confirm() : "\<CR>"

call plug#begin()

" Surround
Plug 'tpope/vim-surround'
" File system tree
Plug 'scrooloose/nerdtree'
Plug 'ryanoasis/vim-devicons'
" Airline (powerline)
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Dracula theme
Plug 'dracula/vim'
" Code completion
Plug 'prabirshrestha/vim-lsp'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'neovim/pynvim'
Plug 'ziglang/zig.vim'

call plug#end()

let g:airline_powerline_fonts = 1
let g:NERDTreeQuitOnOpen = 1

" 4-space indentation
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

colorscheme dracula

au TermClose * call feedkeys("i") " When exit command is run on a terminal, exit

" 4-space indent
set tabstop=4
set shiftwidth=4
set expandtab

