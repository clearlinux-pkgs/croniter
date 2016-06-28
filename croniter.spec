#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : croniter
Version  : 0.3.12
Release  : 21
URL      : https://pypi.python.org/packages/source/c/croniter/croniter-0.3.12.tar.gz
Source0  : https://pypi.python.org/packages/source/c/croniter/croniter-0.3.12.tar.gz
Summary  : croniter provides iteration for datetime object with cron like format
Group    : Development/Tools
License  : MIT
Requires: croniter-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Introduction
============
.. contents::
croniter provides iteration for datetime object with cron like format.

%package python
Summary: python components for the croniter package.
Group: Default

%description python
python components for the croniter package.


%prep
%setup -q -n croniter-0.3.12

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
