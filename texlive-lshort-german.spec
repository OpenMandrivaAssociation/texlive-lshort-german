%global tl_name lshort-german
%global tl_revision 70740

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0c
Release:	%{tl_revision}.1
Summary:	German version of A Short Introduction to LaTeX2e: LaTeX2e-Kurzbeschreibung
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/german
License:	opl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
German version of "A Short Introduction to LaTeX2e":
LaTeX2e-Kurzbeschreibung

