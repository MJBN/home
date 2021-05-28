set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
" #######Put Your Plugin Here#######
Plugin 'VundleVim/Vundle.vim'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'rust-lang/rust.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'racer-rust/vim-racer'
Plugin 'dracula/vim', { 'name': 'dracula' }

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
" Put your non-Plugin stuff after this line

au FileType php setl ofu=phpcomplete#CompletePHP
au FileType ruby,eruby setl ofu=rubycomplete#Complete
au FileType html,xhtml setl ofu=htmlcomplete#CompleteTags
au FileType c setl ofu=ccomplete#CompleteCpp
au FileType css setl ofu=csscomplete#CompleteCSS
colorscheme dracula
let g:rustfmt_autosave = 1
let g:racer_cmd="/home/mjbn/.cargo/bin/racer"
let g:racer_insert_paren = 1
let g:racer_experimental_completer = 1
set  rtp+=/usr/local/lib/python3.9/site-packages/powerline/bindings/vim/
set laststatus=2
set t_Co=256
