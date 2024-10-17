%global packname  CreditMetrics
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          0.0_2
Release:          4
Summary:          Functions for calculating the CreditMetrics risk model
Group:            Sciences/Mathematics
License:          Unlimited
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-2.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    pkgconfig(lapack)

%description
A set of functions for computing the CreditMetrics risk model.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.0_2-2
+ Revision: 774990
- Use proper tarball.
- Bump release.
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:0.0_1-1
+ Revision: 774724
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Fri Dec 25 2009 Jérôme Brenier <incubusss@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 482254
- new version 0.0.2

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-5mdv2010.0
+ Revision: 433080
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-4mdv2009.0
+ Revision: 260129
- rebuild
- rebuild

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-1mdv2008.1
+ Revision: 169935
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-CreditMetrics.

