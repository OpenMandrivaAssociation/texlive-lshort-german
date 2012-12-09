# revision 15878
# category Package
# catalog-ctan /info/lshort/german
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-lshort-german
Version:	20080420
Release:	2
Summary:	German version of A Short Introduction to LaTeX2e: LaTeX2e-Kurzbeschreibung
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/german
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-german.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive lshort-german package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-german/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-german/LaTeX2e-Kurzbeschreibung
%doc %{_texmfdistdir}/doc/latex/lshort-german/README.l2kurz
%doc %{_texmfdistdir}/doc/latex/lshort-german/a.ps
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2gfdl.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k1.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k2.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k3.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k4.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2k6.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2ka.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2ksym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz.tex
%doc %{_texmfdistdir}/doc/latex/lshort-german/l2kurz2.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080420-2
+ Revision: 753471
- Rebuild to reduce used resources

* Mon Nov 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080420-1
+ Revision: 727176
- texlive-lshort-german
- texlive-lshort-german
- texlive-lshort-german
- texlive-lshort-german
- texlive-lshort-german

