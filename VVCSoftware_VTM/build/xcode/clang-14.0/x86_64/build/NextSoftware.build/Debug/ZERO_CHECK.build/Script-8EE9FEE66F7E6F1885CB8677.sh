#!/bin/sh
set -e
if test "$CONFIGURATION" = "Debug"; then :
  cd /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64
  make -f /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64/CMakeScripts/ReRunCMake.make
fi
if test "$CONFIGURATION" = "Release"; then :
  cd /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64
  make -f /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64/CMakeScripts/ReRunCMake.make
fi
if test "$CONFIGURATION" = "RelWithDebInfo"; then :
  cd /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64
  make -f /Users/ruhan/Documents/GitHub/Doctorization/Trabalho-ML/VVCSoftware_VTM/build/xcode/clang-14.0/x86_64/CMakeScripts/ReRunCMake.make
fi

