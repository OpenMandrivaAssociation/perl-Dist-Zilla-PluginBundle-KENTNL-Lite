%define upstream_name    Dist-Zilla-PluginBundle-KENTNL-Lite
%define upstream_version 0.01009803

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Minimal Build-Only replacement for @KENTNL for contributors
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion::Relative)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::EOLTests)
BuildRequires: perl(Dist::Zilla::Plugin::ExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::FakeRelease)
BuildRequires: perl(Dist::Zilla::Plugin::GatherDir)
BuildRequires: perl(Dist::Zilla::Plugin::License)
BuildRequires: perl(Dist::Zilla::Plugin::Manifest)
BuildRequires: perl(Dist::Zilla::Plugin::ManifestSkip)
BuildRequires: perl(Dist::Zilla::Plugin::MetaJSON)
BuildRequires: perl(Dist::Zilla::Plugin::MetaTests)
BuildRequires: perl(Dist::Zilla::Plugin::MetaYAML)
BuildRequires: perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires: perl(Dist::Zilla::Plugin::NextRelease)
BuildRequires: perl(Dist::Zilla::Plugin::PkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PodCoverageTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodSyntaxTests)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires: perl(Dist::Zilla::Plugin::PruneCruft)
BuildRequires: perl(Dist::Zilla::Plugin::TestRelease)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an attempt at one way of solving a common problem when contributing
to things built with Dist::Zilla.

This is done by assuming that the code base that its targeting will *NEVER*
be released in its built form, but close enough to the normal build method
that it's suitable for testing and contributing.

* * Less install time dependencies

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


