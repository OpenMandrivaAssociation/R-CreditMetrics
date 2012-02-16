%global packname  CreditMetrics
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Epoch:            1
Version:          0.0_1
Release:          1
Summary:          Functions for calculating the CreditMetrics risk model
Group:            Sciences/Mathematics
License:          Unlimited
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/CreditMetrics/CreditMetrics_0.0-1.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-CreditMetrics

%description
A set of functions for computing the CreditMetrics risk model.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
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
