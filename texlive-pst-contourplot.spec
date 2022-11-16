Name:		texlive-pst-contourplot
Version:	48230
Release:	1
Summary:	Draw implicit functions using the "marching squares" algorithm
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-contourplot
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-contourplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-contourplot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to draw implicit functions "f(x,y) = 0"
with options for coloring the inside of the surfaces, for
marking the points and arrowing the curve at points chosen by
the user. The package uses the "marching squares" algorithm.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-contourplot
%{_texmfdistdir}/tex/generic/pst-contourplot
%doc %{_texmfdistdir}/doc/generic/pst-contourplot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
