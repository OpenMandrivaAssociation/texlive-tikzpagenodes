# revision 23984
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzpagenodes
# catalog-date 2011-09-17 01:00:07 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-tikzpagenodes
Version:	1.0
Release:	2
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpagenodes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756912
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719745
- texlive-tikzpagenodes
- texlive-tikzpagenodes
- texlive-tikzpagenodes

