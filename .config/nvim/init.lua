--Setting
vim.opt.encoding = "utf-8"
vim.opt.nu = true
vim.opt.wrap = false
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.scrolloff = 8
vim.opt.termguicolors = true
vim.opt.expandtab = true

--VimCMD
vim.cmd("filetype plugin indent on")
vim.cmd("syntax enable")

--Vim-Plug
local Plug = vim.fn['plug#']
vim.call( "plug#begin", "~/.local/share/nvim/plugged")
	Plug 'jiangmiao/auto-pairs'
	Plug 'ap/vim-css-color'
	Plug('neoclide/coc.nvim', {['branch'] = 'release'})
	Plug('dracula/vim', { ['as']= 'dracula' })
	Plug 'airblade/vim-gitgutter'
vim.call( "plug#end")

--VimCMD
vim.cmd("colorscheme dracula")
vim.cmd("highlight Normal guibg=NONE ctermbg=NONE")

