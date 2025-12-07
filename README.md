### NuGet package for PCRE2 - Perl-Compatible Regular Expressions.

| Repository / Package       | URL | Badge |
|----------------------------|-----|----------------|
| Original repository        | https://github.com/PCRE2Project/pcre2/ | [![Latest tag](https://img.shields.io/github/v/tag/PCRE2Project/pcre2?sort=semver)](https://github.com/PCRE2Project/pcre2/) |
| NuGet package              | https://nuget.org/packages/PCRE2/ | [![NuGet version](https://img.shields.io/nuget/v/PCRE2)](https://nuget.org/packages/PCRE2/) |
| nuget-pcre2                | https://github.com/geographika/nuget-pcre2 | - |


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
