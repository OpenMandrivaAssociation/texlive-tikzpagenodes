Name:		texlive-tikzpagenodes
Version:	64967
Release:	2
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpagenodes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides special PGF/TikZ nodes for the text,
marginpar, footer and header area of the current page. They are
inspired by the 'current page' node defined by PGF/TikZ itself.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzpagenodes/tikzpagenodes.sty
%doc %{_texmfdistdir}/doc/latex/tikzpagenodes/README
%doc %{_texmfdistdir}/doc/latex/tikzpagenodes/tikzpagenodes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzpagenodes/tikzpagenodes.dtx
%doc %{_texmfdistdir}/source/latex/tikzpagenodes/tikzpagenodes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
