#!/usr/bin/python

from clang import cindex

f1 = './main.m'

I    = cindex.Index.create()
tu   = I.parse(f1, options=15)
file = cindex.File.from_name(tu, f1)
loc  = cindex.SourceLocation.from_position(tu, file, 1, 8)
c    = cindex.Cursor.from_location(tu, loc)

assert c.kind is cindex.CursorKind.INCLUSION_DIRECTIVE, "Not inclusion directive"

in_file = cindex.conf.lib.clang_getIncludedFile(c)

print in_file
