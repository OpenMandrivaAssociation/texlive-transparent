Name:		texlive-transparent
Version:	64852
Release:	2
Summary:	Using a color stack for transparency with pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/transparent
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pdfTeX and LuaTeX support several color stacks. This package
shows how a separate color stack can be used for transparency,
a property besides color that works across page breaks. If the
PDF management is used it can also be used with other engines,
but without support for page breaks.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/transparent
%{_texmfdistdir}/tex/latex/transparent
%doc %{_texmfdistdir}/doc/latex/transparent

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
