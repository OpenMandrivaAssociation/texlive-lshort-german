Name:		texlive-lshort-german
Epoch:		1
Version:	70740
Release:	1
Summary:	German version of A Short Introduction to LaTeX2e: LaTeX2e-Kurzbeschreibung
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/german
License:	OPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive lshort-german package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-german/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-german/README.l2kurz
%doc %{_texmfdistdir}/doc/latex/lshort-german/allgemeines.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/anhang.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/bilder.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/eingabefile.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/einleitung.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/fontspec.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-german/fontspecbeispiel.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2ksym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz.bib
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/latexmkrc
%doc %{_texmfdistdir}/doc/latex/lshort-german/mathematik.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/ozean.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-german/ozean.svg
%doc %{_texmfdistdir}/doc/latex/lshort-german/schriften.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/seitenaufbau.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/spezialitaeten.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/textsatz.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
