# revision 23984
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzpagenodes
# catalog-date 2011-09-17 01:00:07 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-tikzpagenodes
Version:	1.0
Release:	1
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpagenodes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpagenodes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides special PGF/TikZ nodes for the text,
marginpar, footer and header area of the current page. They are
inspired by the 'current page' node defined by PGF/TikZ itself.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzpagenodes/tikzpagenodes.sty
%doc %{_texmfdistdir}/doc/latex/tikzpagenodes/README
%doc %{_texmfdistdir}/doc/latex/tikzpagenodes/tikzpagenodes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzpagenodes/tikzpagenodes.dtx
%doc %{_texmfdistdir}/source/latex/tikzpagenodes/tikzpagenodes.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
