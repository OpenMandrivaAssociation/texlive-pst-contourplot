%global tl_name pst-contourplot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Draw implicit functions using the marching squares algorithm
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-contourplot
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-contourplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-contourplot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to draw implicit functions "f(x,y) = 0" with options
for coloring the inside of the surfaces, for marking the points and
arrowing the curve at points chosen by the user. The package uses the
"marching squares" algorithm.

