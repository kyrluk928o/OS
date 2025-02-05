Name: count_files
Version: 1.0
Release: 1%{?dist}
Summary: Скрипт для підрахунку файлів в каталозі /etc
License: GPLv3
Source0: count_files.sh

%description
Скрипт для підрахунку файлів у каталозі /etc, виключаючи директорії та символічні посилання.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh

%changelog
* Tue Jan 4 2025 Developer <kirichenkobogdan928@gmail.com> 1.0-1
- Initial release.
