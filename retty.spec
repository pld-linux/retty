Summary:	retty - attach processes running on other terminals
Summary(pl.UTF-8):   retty - podłączanie się do procesów działających na innych terminalach
Name:		retty
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://pasky.or.cz/~pasky/dev/retty/%{name}-%{version}.tar.bz2
# Source0-md5:	f40841b7b8d2b99693874b0bfdb37564
URL:		http://pasky.or.cz/~pasky/dev/retty/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
retty is a tiny tool that lets you attach processes running on other
terminals. So you were running that mutt outside of screen at your
home machine and now wanna check your mail? Attach it with retty, do
whatever you want, detach it again and everything is as it was before.
You don't have to run them all in screen just in case.

%description -l pl.UTF-8
retty to małe narzędzie pozwalające podłączyć się do procesów
działających na innych terminalach. Jeśli na przykład uruchomiliśmy
mutta nie na screenie na domowej maszynie i chcemy sprawdzić zdalnie
pocztę, możemy uruchomić retty, zrobić co tylko chcemy, odłączyć się i
wszystko będzie tak, jak wcześniej. Nie trzeba w tym celu uruchamiać
programów na screenie.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install blindtty retty $RPM_BUILD_ROOT%{_bindir}
install retty.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/blindtty
%attr(755,root,root) %{_bindir}/retty
%{_mandir}/man1/retty.1*
