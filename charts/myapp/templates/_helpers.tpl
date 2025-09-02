{{- define "myapp.name" -}}myapp{{- end -}}
{{- define "myapp.fullname" -}}{{ printf "%s-%s" .Release.Name (include "myapp.name" .) | trunc 63 | trimSuffix "-" }}{{- end -}}
