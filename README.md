### NuGet package for PCRE2 - Perl-Compatible Regular Expressions.

PCRE2 NuGet - https://www.nuget.org/packages/PCRE2/
PCRE2 library - https://github.com/PCRE2Project/pcre2

Usage (from powershell):
```powershell
# Required dependency.
pip install conan

# Set PCRE2 version.
$env:PCRE2_VERSION="10.47"

# Download source.
conan source

# Build and install to `package` folder.
conan build

# Pack NuGet package.
# Use `-NoPackageAnalysis` to suppress warnings, because we're making cmake files.
nuget pack pcre2.nuspec -Version $env:PCRE2_VERSION -NoPackageAnalysis
```
