%global tl_name tikzpagenodes
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A single TikZ node for the whole page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpagenodes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides special PGF/TikZ nodes for the text, marginpar,
footer and header area of the current page. They are inspired by the
'current page' node defined by PGF/TikZ itself.

