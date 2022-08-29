map ,d :NERDTreeToggle<cr>
map ,r :te make run<cr>:norm G<cr>
" Go-to commands
map gd <Plug>(coc-definition)
map gi <Plug>(coc-implementation)
map gr <Plug>(coc-references)

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

call plug#end()

let g:airline_powerline_fonts = 1
let g:NERDTreeQuitOnOpen = 1

colorscheme dracula

au TermClose * call feedkeys("i") " When exit command is run on a terminal, exit
