--Vim-Plug
local Plug = vim.fn['plug#']
vim.call( "plug#begin", "~/.local/share/nvim/plugged")
    Plug('jiangmiao/auto-pairs')
    Plug('ap/vim-css-color')
    Plug('neoclide/coc.nvim', {['branch'] = 'release'})
    Plug('dracula/vim', { ['as']= 'dracula' })
    Plug('airblade/vim-gitgutter')
vim.call( "plug#end")

--VimCMD
vim.cmd("colorscheme dracula")
vim.cmd("highlight Normal guibg=NONE ctermbg=NONE")
